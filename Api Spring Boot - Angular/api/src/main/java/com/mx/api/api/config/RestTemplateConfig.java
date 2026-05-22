package com.mx.api.api.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;


//Definimos un Bean para poder inyectarlo en el cualquier parte sin instanciarlo
@Configuration // Con esta anotación indicamos a spring que es una clase de configuración, es decir El Bean que vamos a crear
public class RestTemplateConfig {

    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }

}