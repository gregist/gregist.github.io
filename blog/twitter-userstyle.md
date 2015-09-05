---
layout:      post
title:       twitter userstyle
date:        2015-09-05
update_date: 
summary:     
categories:  blog
permalink:   /blog/twitter-userstyle/
---

```
@-moz-document domain("twitter.com") {
	.dashboard,
	.content-main
	{
		width: auto !important;
		float: none !important;
	}

	.wtf-module,
	.trends,
	.site-footer,
	.Footer,
	.profile-header-inner,
	.newest-members-module,
	.stream-item-footer a.details,
	.module.DashboardProfileCard,
	.js-nav-links,
	div.component:nth-child(3),
	.stream-item-footer a.details,
	.media-not-displayed
	{
		display: none !important;
	}

	.cards-base img, .permalink-tweet div.tweet-media img, div.tweet-media .cards-base img{
		max-width: 53%;
	}
	
	.TwitterPhoto-media,
	.cards-base .media-forward {
		max-height: none !important;
	}

	.TwitterPhoto-media img,
	.cards-base .media-forward img {
		margin-top: auto !important;
	}
}
```

features:

* disable image cropping
* hide redundant modules
* full width timeline
* half width img