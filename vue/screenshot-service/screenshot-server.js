const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
// eslint-disable-next-line import/no-extraneous-dependencies
const puppeteer = require('puppeteer');

const app = express();
const port = 8079;

app.use(cors());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('*', async (req, res) => {
  console.log(req.params);
  const path = req.params['0'];
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/chromium-browser',
    headless: true,
    devtools: false,
    args: [
      '--no-sandbox',
      '--disable-dev-shm-usage'
      // '--remote-debugging-port=9222',
      // '--remote-debugging-address=0.0.0.0'
    ]
  });

  let screenshotUrl = `http://localhost:8080${path}?screenshot`;
  if (req.query.thumbnail) {
    screenshotUrl += '&thumbnail';
  }

  const page = await browser.newPage();
  page.setViewport({
    width: 1200,
    height: 900,
    deviceScaleFactor: 2,
    isLandscape: true
  });
  await page.goto(screenshotUrl);
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
