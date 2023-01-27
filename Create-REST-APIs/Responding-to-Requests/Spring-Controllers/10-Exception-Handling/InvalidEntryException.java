package com.codecademy.ccapplication;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value = HttpStatus.NOT_FOUND, reason = "Invalid Entry. Please try again.")
public class InvalidEntryException extends RuntimeException {

    public InvalidEntryException() {

        super();
    }
}
