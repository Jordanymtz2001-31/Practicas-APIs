package com.mx.api.api.Dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import lombok.Data;


//Mapeamos las propiedades de la API
@JsonIgnoreProperties(ignoreUnknown = true) // Ignorar propiedades desconocidas
@Data
public class ProductoDto {

    private Long id;
    private String title;
    private Double price;
    private String description;
    private String category;
    private String image;
    private RatingDto rating; 

}
