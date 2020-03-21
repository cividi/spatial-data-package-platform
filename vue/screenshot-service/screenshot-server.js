const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const puppeteer = require('puppeteer');

const app = express();
const port = 8079;

app.use(cors());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/screenshot/:hash', async (req, res) => {
  console.log(req.params);
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/chromium-browser',
    headless: true,
    devtools: true,
    args: [
      '--no-sandbox',
      '--disable-dev-shm-usage',
      '--remote-debugging-port=9222',
      '--remote-debugging-address=0.0.0.0'
    ]
  });
  const page = await browser.newPage();
  page.setViewport({
    width: 800,
    height: 800
  });
  await page.goto(`http://localhost:8080/de/${req.params.hash}/screenshot/`);
  await page.waitForSelector('#mapinfo .v-list-item__title');
  const screenshotBuffer = await page.screenshot({ encoding: 'binary' });
  await browser.close();
  res.writeHead(200, {
    'Content-Type': 'image/png',
    'Content-disposition': 'attachment;filename=screenshot.png',
    'Content-Length': screenshotBuffer.length
  });
  res.end(Buffer.from(screenshotBuffer, 'binary'));
});

app.listen(port, () => console.log(`screenshot-server on port ${port}`));
