---
layout:      post
title:       Twitter Userstyle
date:        2015-09-05
update_date: 
summary:     
categories:  blog
permalink:   /blog/Twitter-Userstyle/
---

	@-moz-document domain("twitter.com") {
		div#page-container.wrapper {
			width: 997px !important;
		}
		
		.dashboard,
		.content-main,
		.u-lg-size2of3 {
			width: 811px !important;
		}
		
		.topbar {
			position: absolute;
		}
		
		.ScrollBump,
		.PhotoRail,
		div.component:nth-child(3),
		.WhoToFollow.is-visible,
		.wtf-module,
		.trends,
		.site-footer,
		.Footer,
		.profile-header-inner,
		.newest-members-module,
		.stream-item-footer a.details,
		.module.DashboardProfileCard,
		.js-nav-links,
		.stream-item-footer a.details,
		.media-not-displayed {
			display: none !important;
		}

		.cards-base img, 
		.permalink-tweet div.tweet-media img, 
		div.tweet-media .cards-base img {
			max-width: 809px;
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


features:

* hide redundant modules
* full width timeline
* full height images