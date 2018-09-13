# -*- coding: utf-8 -*-
import scrapy
#from pensador.items import PensadorItem


class FrasesSpider(scrapy.Spider):
    name = 'frases'
    #allowed_domains = ['www.pensador.com/schopenhauer_frases/']
    start_urls = ['https://www.pensador.com/schopenhauer_frases/']

    def parse(self, response):
        
        #item = PensadorItem()
        
        frases = response.css('p[class^="frase"] ::text').extract()
        
        for frase in frases:
            #item['frase'] = frase
            #print(item['frase'])
            yield {'frase': frase}


        dominio = "https://www.pensador.com"
        pagina = response.css('a[class="nav"] ::attr(href)').extract()
        pagina = pagina[-1]
        proxima_pagina = dominio + pagina

        if proxima_pagina:
            self.log('***** PRÓXIMA PÁGINA ****** => {}'.format(proxima_pagina))
            yield scrapy.Request(url=proxima_pagina, callback=self.parse)

