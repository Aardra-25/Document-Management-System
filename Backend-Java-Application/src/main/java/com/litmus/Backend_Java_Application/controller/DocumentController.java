package com.litmus.Backend_Java_Application.controller;

import com.litmus.Backend_Java_Application.model.Document;
import com.litmus.Backend_Java_Application.repository.DocumentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/documents")
public class DocumentController {

    @Autowired
    private DocumentRepository documentRepository;

    @GetMapping
    public List<Document> getAllDocuments() {
        return documentRepository.findAll();
    }
}