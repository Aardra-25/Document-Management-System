package com.litmus.Backend_Java_Application.model;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Getter
@Entity
public class Document {
    // Getters and setters

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column
    private String documentName;
    @Column
    private String filePath;


    public void setName(String document_name) {
        this.documentName = document_name;
    }


    public String getDocumentName() {
        return documentName;
    }

    public void setDocumentName(String documentName) {
        this.documentName = documentName;
    }
    public void setFile(String file_path){
        this.filePath = file_path;
    }
    public String getFilePath() {
        return filePath;
    }

    public void setFilePath(String filePath) {
        this.filePath = filePath;
    }


}


