-------------------------------------------------------------------------------
-- HTTP Accept-Language header handler                                       --
-- @originalAuthor: f.ghibellini@gmail.com                                   --
-- @originalRepository: https://github.com/fghibellini/nginx-http-accept-lang--
-- @modifiedBy: marian.hello@mapilary.com                                    --
-- @gist: https://gist.github.com/mauron85/47ed1075262d9e020fe2              --
-- @license: MIT                                                             --
-- @requires:                                                                --
-- @description:                                                             --
--     returns language with greatest quality                                --
--     value according to RFC:2616                                           --
-- @example configuration:                                                   --
--                                                                           --
--     server {                                                              --
--         listen 8080 default_server;                                       --
--         index index.html index.htm;                                       --
--         server_name localhost;                                            --
--                                                                           --
--         root usr/share/nginx/html;                                        --
--                                                                           --
--         location = / {                                                    --
--             # $lang_sup holds comma separated languages supported by site --
--             # if no match first will be used (en) in this case            --
--             set $lang_sup = "en,sk"                                       --
--             set_by_lua_file $lang_accept /etc/nginx/lang.lua $lang_sup;   --
--             rewrite (.*) $scheme://$server_name/$lang_accept$1;           --
--         }                                                                 --
--     }                                                                     --
--                                                                           --
-------------------------------------------------------------------------------

function inTable(tbl, item)
    for key, value in pairs(tbl) do
        if value == item then return key end
    end
    return false
end

function string:split( inSplitPattern, outResults )
   if not outResults then
      outResults = { }
   end
   local theStart = 1
   local theSplitStart, theSplitEnd = string.find( self, inSplitPattern, theStart )
   while theSplitStart do
      table.insert( outResults, string.sub( self, theStart, theSplitStart-1 ) )
      theStart = theSplitEnd + 1
      theSplitStart, theSplitEnd = string.find( self, inSplitPattern, theStart )
   end
   table.insert( outResults, string.sub( self, theStart ) )
   return outResults
end

local lang_sup = {"en"}
if ( ngx.arg[1] ~= nil ) then
    lang_sup = ngx.arg[1]:split(",")
end

local lang_header = ngx.var.http_accept_language
if ( lang_header == nil ) then
    return lang_sup[1]
end

local cleaned = ngx.re.sub(lang_header, "^.*:", "")
local options = {}
local iterator, err = ngx.re.gmatch(cleaned, "\\s*([a-z]+(?:-[a-z])*)\\s*(?:;q=([0-9]+(.[0-9]*)?))?\\s*(,|$)", "i")
for m, err in iterator do
    local lang = m[1]
    local priority = 1
    if m[2] ~= nil then
        priority = tonumber(m[2])
        if priority == nil then
        priority = 1
        end
    end
    table.insert(options, {lang, priority})
end

table.sort(options, function(a,b) return b[2] < a[2] end)

for index, lang in pairs(options) do
    if inTable(lang_sup, lang[1]) then
        return lang[1]
    end
end

return lang_sup[1]