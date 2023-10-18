# congressional-captcha

Model legislation written by industry groups, think tanks, and corporations are introduced by state lawmakers every legislative session. A 2019 analysis of over 1 million bills found that nearly 10,000 bills copied off of model legislation were introduced over an 8 year period. The goal of this project is to produce a pipeline to reproduce [this analysis](https://www.azcentral.com/in-depth/news/local/arizona-investigations/2019/04/04/abortion-gun-laws-stand-your-ground-model-bills-conservatives-liberal-corporate-influence-lobbyists/3361759002/) with updated legislative data at a smaller scale (the linked report states their analysis required ~150 computers' worth of computing power and several months of runtime). 

Tentatitive steps for this project: 
1. Obtain legislative data using the [LegiScan]([url](https://legiscan.com/legiscan)https://legiscan.com/legiscan) API. LegiScan updates legislative information in real time and tracks bills from all statehouses and U.S. Congress. Obtain model bill data from [ALEC](https://alec.org/model-policy/?alec_search_term=&alec_post_type%5B%5D=model-policy&alec_year=&alec_p2p%5B%5D=&alec_meta%5B%5D=&alec_meta%5B%5D=&alec_term%5B%5D=&in_page_search=1). 
2. Plan to standardize data/extract text. I'm sure that different states upload bills as PDFs, Word files, web pages, etc.
3. Choose a method for analyzing text similarity for a subset of bills (same topic, keywords, etc.)
4. Visualize semantic similarity (interactively?) across different topics
