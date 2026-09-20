#!/usr/bin/env python3
"""Build or verify the physics archive, retaining links to the mathematics archive."""
from math_import_content import PAGES as MATH_PAGES
from physics_import_content import GROUPS, PAGES, SIGNALS, SUPPLEMENTS
from scrapbox_import import configure, main

if __name__ == '__main__':
    cross_links = {title: f'math/{page["group"]}/{page["slug"]}.md'
                   for title, page in MATH_PAGES.items()}
    configure('physics', '物理学', GROUPS, PAGES, SIGNALS, SUPPLEMENTS,
              '44 new overview physics pages and 7 related pages; one shared overview link is archived under math',
              cross_links)
    main()
