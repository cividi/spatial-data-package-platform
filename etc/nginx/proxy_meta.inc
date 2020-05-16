        if (!-f $request_filename) {
            header_filter_by_lua_block {
                ngx.header.content_length = nil
            }
            set_by_lua_file $meta "/etc/nginx/conf.d/meta.lua";
            body_filter_by_lua_block {
                ngx.arg[1] = ngx.arg[1]:gsub('<meta replace>', ngx.var.meta)
            }
            proxy_pass http://vue-dev;
            break;
        }
