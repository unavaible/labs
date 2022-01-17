package com.example.dzrip;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class Post {
    @SerializedName("id_company")
    @Expose
    private int idCompany;
    @SerializedName("name_company")
    @Expose
    private String nameCompany;
    @SerializedName("foundation_year")
    @Expose
    private int foundationYear;
    @SerializedName("specialization")
    @Expose
    private String specialization;

    public Post(String name, String descript, int year)
    {
        this.nameCompany = name;
        this.specialization = descript;
        this.foundationYear = year;
    }

    public int getIdCompany() {
        return idCompany;
    }

    public String getNameCompany() {
        return nameCompany;
    }

    public int getFoundationYear() {
        return foundationYear;
    }

    public String getSpecialization() {
        return specialization;
    }
}
