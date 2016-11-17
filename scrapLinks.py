def scrapLinks(s):
	count = 0
	while True:
		startLink = s.find("<a href=", count)
		if startLink == -1:
			print 'empty'
		firstQuote = s.find('"', startLink)+1
		lastQuote = s.find('"', firstQuote+1)
		page = s[firstQuote:]
		url = s[firstQuote:lastQuote]
		count = 1+startLink

		print url, count

		if startLink == -1:
			break

	# return url, count,

# def links(s):
# 	startQuote = s.find('"')+1
# 	endQuote = s.find('"', startQuote+1)
# 	links = s[startQuote:endQuote]
# 	return links


s = '''
<a href="http://meta.stackoverflow.com"
       class="site-link js-gps-track"
       data-id="552"
       data-gps-track="
            site.switch({ target_site:552, item_type:3 }),
        site_switcher.click({ item_type:4 })">
        <div class="site-icon favicon favicon-stackoverflowmeta" title="Meta Stack Overflow"></div>
        Meta Stack Overflow
    </a>
<a href="http://meeeeeta.stackoverflow.com"
aqui


'''
print scrapLinks(s)