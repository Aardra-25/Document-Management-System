package com.litmus.Backend_Java_Application.repository;

import com.litmus.Backend_Java_Application.model.Document;
import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface DocumentRepository extends JpaRepository<Document, Long> {

    Long id(Long id);

    List<Document> Id(Long id);

    List<Document> getDocumentsById(Long id);


    @Query("select d from Document d where d.documentName = :documentName")
    List<Document> findByDocumentName(String documentName);

    @Query("select d from Document d where d.projectName = :projectName")
    List<Document> findByProjectName(String projectName);

}



