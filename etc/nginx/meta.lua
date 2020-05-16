
local file_meta, err = io.open("/var/services/django/media/snapshot-meta/" .. ngx.var.hash ..".html", "r")
if file_meta then
    local content = file_meta:read("*all")
    return content
else
    return ""
end
