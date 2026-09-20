#!/usr/bin/env python3
"""Build or verify chemistry sources, with links to existing math and physics."""
from math_import_content import PAGES as MATH_PAGES
from physics_import_content import PAGES as PHYSICS_PAGES
from chemistry_import_content import GROUPS, PAGES, SIGNALS, SUPPLEMENTS
from scrapbox_import import configure, main

if __name__ == '__main__':
    cross_links = {
        title: f'{section}/{page["group"]}/{page["slug"]}.md'
        for section, pages in [('math', MATH_PAGES), ('physics', PHYSICS_PAGES)]
        for title, page in pages.items()
    }
    configure('chemistry', '化学', GROUPS, PAGES, SIGNALS, SUPPLEMENTS,
              '12 chemistry, materials, and adjacent life-science pages selected from the public catalog and source links; existing physics pages remain cross-references',
              cross_links)
    main()
