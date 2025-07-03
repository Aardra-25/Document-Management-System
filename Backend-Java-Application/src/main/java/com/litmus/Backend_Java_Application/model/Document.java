package com.litmus.Backend_Java_Application.model;

import jakarta.persistence.*;
import lombok.Getter;

@Getter
@Entity
public class Document {
    // Getters and setters
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    public void setId(Long id) { this.id = id; }

    public void setName(String name) { this.name = name; }
}
