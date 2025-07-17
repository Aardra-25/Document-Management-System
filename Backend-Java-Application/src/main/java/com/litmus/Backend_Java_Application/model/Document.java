package com.litmus.Backend_Java_Application.model;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.time.LocalDateTime;

@Getter
@Setter
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
    @Column
    private String projectName;

    @Column
    private String createdBy;
    @CreationTimestamp
    private LocalDateTime createdAt;

    private LocalDateTime lastEdited;

    @PrePersist
    protected void onCreate() {
        lastEdited = LocalDateTime.now();
    }

    @PreUpdate
    protected void onUpdate() {
        lastEdited = LocalDateTime.now();
    }

}


