package com.litmus.Backend_Java_Application.Backend_Controller;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;

@RestController
public class BackendController {
    @GetMapping("/document")
    public String DocumentManagementSystem() {
        return "Documents would be received";
    }
}
