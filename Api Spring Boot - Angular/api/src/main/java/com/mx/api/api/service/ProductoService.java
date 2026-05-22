package com.mx.api.api.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpMethod;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.mx.api.api.Dto.ProductoDto;

@Service
public class ProductoService {

    @Autowired
    private RestTemplate restTemplate;

    public List<ProductoDto> getAllProductos() {
        String url = "https://fakestoreapi.com/products";

        return restTemplate.exchange( // Con exchange indicamos que va a hacer una petición (Permite manualmente hacer peticiones HTTP)
                url,
                HttpMethod.GET,
                null, // No enviamos ningún body
                new ParameterizedTypeReference<List<ProductoDto>>() {} // Con ParameterizedTypeReference indicamos que lo que obtenemos de la API, convierta el JSON en una lista de Tipo Productos
        ).getBody(); // El método getBody nos devuelve el cuerpo o no de la petición
    }

}
