package com.mx.api.api.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.mx.api.api.service.ProductoService;

@RestController
@CrossOrigin(origins = "http://localhost:4200")
public class ProductoController {

    @Autowired // Con la anotación @Autowired indicamos que inyecte la dependencia, sin la necesidad de un constructor
    private ProductoService productoSe;

    @GetMapping("/api/products")
    public ResponseEntity<?> listarProducts() {
        return ResponseEntity.ok(productoSe.getAllProductos());
    }

}
