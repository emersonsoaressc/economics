
mkdir -p ~ /.streamlit/

echo  " \
[servidor] \ n \
porta = $ PORT \ n \
enableCORS = false \ n \
headless = true \ n \
\ n \
"  >  ~ /.streamlit/config.toml