---
layout:      post
title:       Userstyles
date:        2015-09-05
update_date: 2015-09-09
summary:     
categories:  blog
permalink:   /blog/Userstyles/
---

### Twitter

	@-moz-document domain("twitter.com") {
		div#page-container.wrapper {
			width: 997px !important;
		}
		
		.GridTimeline,
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

### about:reader

	@-moz-document url-prefix("about:reader") {
		#container {
			max-width: 701px !important;
		}
	}