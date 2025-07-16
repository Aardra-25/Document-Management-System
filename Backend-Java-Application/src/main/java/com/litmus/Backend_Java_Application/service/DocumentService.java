package com.litmus.Backend_Java_Application.service;

/*
import com.litmus.Backend_Java_Application.exception.ResourceNotFoundException;*/
import com.litmus.Backend_Java_Application.exception.ResourceNotFoundException;
import com.litmus.Backend_Java_Application.model.Document;
import com.litmus.Backend_Java_Application.repository.DocumentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class DocumentService {

    @Autowired
    private DocumentRepository documentRepository;

    public Optional<Document> findById(Long id) {
        return documentRepository.findById(id);
    }

    public List<Document> findAllById(List<Long> ids) {
        return documentRepository.findAllById(ids);

        }

    public Document saveDocument(Document document) {
        return documentRepository.save(document);
    }

    public String deleteById(Long id){
        documentRepository.deleteById(id);
        return "Document with ID " + id + " deleted successfully.";
    }


    public List<Document> findByDocumentName(String documentName) {

        return documentRepository.findByDocumentName(documentName);
    }

    public void deleteDocument(Long id) {
        Document document = documentRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Document not found with ID: " + id));
        documentRepository.delete(document);
    }
}



