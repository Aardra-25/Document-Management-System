package com.litmus.Backend_Java_Application.service;


import com.litmus.Backend_Java_Application.model.Document;
import com.litmus.Backend_Java_Application.repository.DocumentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DocumentService {

    @Autowired
    DocumentRepository documentRepository;


    public List<Document> findAllDocuments(){

        return documentRepository.findAll();
    }
}