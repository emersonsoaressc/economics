mkdir -p ~ / .streamlit /
echo "\ 
[geral] \ n \ 
email = \" emerson.soares.sc@gmail.com \ "\ n \ 
"> ~ / .streamlit / credentials.toml
echo "\ 
[servidor] \ n \ 
headless = true \ n \ 
enableCORS = false \ n \ 
port = $ PORT \ n \ 
"> ~ / .streamlit / config.toml