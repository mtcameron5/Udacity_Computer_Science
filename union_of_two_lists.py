def union(list_one, list_two):
    union = list_one
    for x in list_two:
        if x in list_two and x not in list_one:
            union.append(x)
    return union



def get_all_links(page):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url: 
			page = page[endpos:]
			links.append(url)
		else:
			break 
	return links


#def crawl_web(seed_page):
#	to_crawl = get_all_links(seed_page)
#	while to_crawl.len > 0:
#		crawled = []
#		new_link = to_crawl.pop()
#		if 
