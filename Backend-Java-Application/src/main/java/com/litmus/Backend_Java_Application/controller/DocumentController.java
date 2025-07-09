package com.litmus.Backend_Java_Application.controller;

import com.litmus.Backend_Java_Application.model.Document;
import com.litmus.Backend_Java_Application.service.DocumentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

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

   /* @PostMapping("/new")
    public Document addDocument(@RequestBody Document document) {
        return documentService.saveDocument(document);
    }
*/
    @DeleteMapping("/{id}")
    public String deleteDocument(@PathVariable Long id) {
        return documentService.deleteById(id);
    }


    @GetMapping("/projectName/{documentName}")
    public List<Document> findByDocumentName(@PathVariable("documentName") String documentName) {
        System.out.println(documentName);
        return documentService.findByDocumentName(documentName);
    }
}




