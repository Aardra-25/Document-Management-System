package com.litmus.Backend_Java_Application.repository;

import com.litmus.Backend_Java_Application.model.Document;
import org.springframework.data.jpa.repository.JpaRepository;

public interface DocumentRepository extends JpaRepository<Document, Long> {
}
