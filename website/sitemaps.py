from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"  # Optional: Tells Google how often pages change
    priority = 0.8        # Optional: Tells Google page importance (0.0 to 1.0)

    def items(self):
        # Match your exact url names: 'index', 'about', 'contact', 'feedback', 'work'
        return ['index', 'about', 'contact', 'feedback', 'work']

    def location(self, item):
        return reverse(item)
