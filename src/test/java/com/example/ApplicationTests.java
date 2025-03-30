package com.example;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest(classes = Application.class)  // Pointing to the main Application class
public class ApplicationTests {

    @Test
    public void contextLoads() {
        // This test will check if the application context loads correctly.
    }
}
