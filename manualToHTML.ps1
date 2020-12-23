pandoc `
    --metadata title="Anki Manual 20201222" `
    --filter ..\fix-links-single-file.py `
    --pdf-engine=xelatex `
    -s $(cat ..\pandocIncludes.txt) `
    -f markdown-raw_tex `
    -t html5 `
    -o ..\AnkiManual-20201222.html