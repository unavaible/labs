package com.example.dzrip;

import java.util.List;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Response;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.PUT;
import retrofit2.http.Path;
import retrofit2.http.Query;

public interface JSONPlaceHolderApi {
    @GET("/it_company/")
    public Call<List<Post>> getAllPosts();

    @DELETE("/it_company/{id}/")
    public Call<ResponseBody> deletePost(@Path("id") int lang_id);

    @POST("/it_company/")
    public Call<Post> createPost(@Body Post post);

    @PUT("/it_company/{id}/")
    public Call<Post> updatePost(@Path("id") int lang_id, @Body Post post);
}
