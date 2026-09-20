#!/usr/bin/env python3
"""Build or verify the mathematics archive. Run --check without local API caches."""
from math_import_content import GROUPS, PAGES, SIGNALS, SUPPLEMENTS
from scrapbox_import import configure, main

if __name__ == '__main__':
    configure('math', '数学', GROUPS, PAGES, SIGNALS, SUPPLEMENTS,
              '45 overview math pages and 19 explicitly selected related pages')
    main()
