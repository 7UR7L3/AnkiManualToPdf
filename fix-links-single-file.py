# thanks https://stackoverflow.com/a/41005658
# thanks https://stackoverflow.com/a/48540492
# thanks https://stackoverflow.com/a/48172069
# thanks https://stackoverflow.com/a/26561057
# thanks https://github.com/jgm/pandoc/issues/6595#issuecomment-670132702
# thanks https://tex.stackexchange.com/a/234796

import panflute as pf
import re

def action(elem, doc):
    if isinstance(elem, pf.Link) and elem.url == "/": elem.url = "intro.md"
    if isinstance(elem, pf.Link) and re.fullmatch( r".+\.md(#.+)?", elem.url ):
        newUrl = elem.url;

        m = re.fullmatch( r".+\.md", elem.url ); # link to header on first line of `blah.md`
        line = "default"
        try:
            if m and m.group():
                with open( m.group(), "r", encoding="utf8" ) as f:
                    line = f.readline();
                    if line.startswith( "# " ): # see pandoc/src/Text/Pandoc/Readers/Markdown.hs:mmdHeaderIdentifier for how you're supposed to do this
                        newUrl = "#" + line[2:].lower().replace( "/", "" ).replace( "&", "" ).strip();
                        newUrl = re.sub( r" +", "-", newUrl );
        except Exception as e:
            newUrl = "FILELINK " + m.group() + " NO BUENO " + line + "|" + str(e);

        m = re.fullmatch( r"(.+\.md)?#(.+)", elem.url ); # link to #foo for `blah.md#foo` (no easy way to tell which #foo-n really.. can hardcode exceptions ig)
        if m and m.groups(): newUrl = "#" + m.groups()[-1].strip();

        if newUrl == "#media": newUrl = "#media-1"; # default links to the major media section instead of the sync subsection. crude hardcoded exception
        elem.url = newUrl;
        return elem;

if __name__ == '__main__':
    pf.run_filter(action)


"""
-- fix-links-single-file.lua
function Link (link)
  link.target = link.target:gsub('.+%.md%#(.+)', '#%1')
  return link
end
"""