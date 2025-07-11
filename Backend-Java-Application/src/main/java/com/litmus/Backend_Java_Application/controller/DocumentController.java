package com.litmus.Backend_Java_Application.controller;

import com.litmus.Backend_Java_Application.model.Document;
import com.litmus.Backend_Java_Application.service.DocumentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/documents")
public class DocumentController {

    @Autowired
    private DocumentService documentService;

    @GetMapping("/{id}")
    public Document findAllById(@PathVariable Long id) {
        return documentService.findById(id)
                .orElseThrow(() -> new RuntimeException("Document not found with id: " + id));
    }

    @GetMapping("/get-by-ids")
    public List<Document> findAllById(@RequestParam List<Long> ids) {
        return documentService.findAllById(ids);
    }

    @PostMapping("/new")
    public Document addDocument(@RequestBody Document document) {
        return documentService.saveDocument(document);
    }

    @DeleteMapping("/{id}")
    public String deleteDocument(@PathVariable Long id) {
        return documentService.deleteById(id);
    }

    @PutMapping("/document/{id}")
    public ResponseEntity<Document> updateDocument(@PathVariable Long id, @RequestBody Document updatedDocument) {
        Optional<Document> existing = documentService.findById(id);
        if (existing.isPresent()) {
            Document document = existing.get();
            document.setDocumentName(updatedDocument.getDocumentName());
            document.setFilePath(updatedDocument.getFilePath());

            Document saved = documentService.saveDocument(document);
            return ResponseEntity.ok(saved);
        } else {
            return ResponseEntity.notFound().build();
        }
    }



    @GetMapping("/projectName/{documentName}")
    public List<Document> findByDocumentName(@PathVariable("documentName") String documentName) {
        System.out.println(documentName);
        return documentService.findByDocumentName(documentName);
    }
}




