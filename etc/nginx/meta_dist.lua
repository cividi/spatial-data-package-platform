local file_meta, err = io.open("/var/services/django/media/snapshot-meta/" .. ngx.var.hash ..".html", "r")
local file_app, err = io.open("/var/services/django/static/dist/app.html", "r")

local body = file_app:read("*all")

if file_meta then
    local meta_replace = file_meta:read("*all")
    body = body:gsub('<meta replace>', meta_replace)
end

ngx.say(body)
