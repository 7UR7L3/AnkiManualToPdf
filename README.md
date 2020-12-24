# AnkiManualToPdf
Pandoc filter and scripts to convert https://github.com/ankitects/anki-manual docsify site to standalone hyperlinked pdf/epub/html/anything supported by pandoc. Pretty crude but pretty straightforward.

Can run example script `..\manualToHTML.ps1` from `.\anki-manual\` to regenerate.

---

I have a nice ereader that plays much nicer with pdfs than it does with websites. I wanted to comfortably read the Anki manual.

Anki moved from the nice single page docs to docsify. Docsify has no way to export to pdf or even to static html (maybe that will change eventually https://github.com/docsifyjs/docsify/issues/136).

- docsify-server-renderer refused to work
- https://github.com/engaugusto/docsify-to-pdf failed to properly hyperlink between md files (though this got very close to ideal)
- weasyprint and wkhtmltopdf both spit out a single page blank nothingness
- gitbook wouldn't export to a pdf for free
- calibre's ebook-convert is baffling
- mkdocs-pdf-export-plugin failed to properly hyperlink between md files

So I gave up and "did it myself" with pandoc.

---

- hardcoded `pandocIncludes.txt` ripped from `anki-manual\_sidebar.md`
- hardcoded `#media` to `#media-1` exception
- assumes that links to `foo.md` have an h1 `# Foo Title` header on the first line, and link to that corresponding `#foo-title`
- assumes that links to `foo.md#bar` link to a unique `#bar` and doesn't do anything clever to work out `#bar-n`
- doesn't change anything about `#baz` links

I probably should have dug into and fixed the existing `docsify-to-pdf` hyperlinking but I only had that realization shortly after pandoc was spitting out pretty much ideal stuff. `docsify-to-pdf\src\markdown-combine.js` is probably more or less what the pandoc filter does.

But really I should combine the ideas and either leverage docsify's own code to link things up, or see if pandoc filters have access to the entire merged input so that I could properly deduce the linkages. Cause pandoc output flexibility is ideal.
