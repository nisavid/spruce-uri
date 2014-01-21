"""Codecs

These objects deal with encoding and decoding data in URIs and related
formats.

Several of these objects are simply aliases of objects from
:mod:`urllib` or :mod:`urlparse`.  The names given here are intended to
be more correct or canonical (per applicable standards such as
:rfc:`3986`), to more clearly describe functionality, to follow modern
Python naming conventions, and to avoid inaccurate apparent restrictions
to URLs (as opposed to URIs generally).

"""

__copyright__ = "Copyright (C) 2014 Ivan D Vasin"
__docformat__ = "restructuredtext"

from urllib \
    import quote as pct_encoded, \
           quote_plus as pct_plus_encoded, \
           unquote as pct_decoded, \
           unquote_plus as pct_plus_decoded, \
           urlencode as urlencoded
from urlparse \
    import parse_qs as parse_urlencoded, \
           urljoin as join, \
           urlsplit as split, \
           urlunsplit as unsplit
