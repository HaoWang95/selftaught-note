This note will include __CrudRepository__, __JpaRepository__ and __PagingAndSortingRepository__.

The **JpaRepository** extends the **PagingAndSortingRepository**.

```java
// also, please note that the extended QueryByExampleExecutor
public interface JpaRepository<T, ID> extends PagingAndSortingRepository<T, ID>, QueryByExampleExecutor<T> {}

```

The **PagingAndSortingRepository** extends the **CrudRepository**. 
```java
public interface PagingAndSortingRepository<T, ID> extends CrudRepository<T, ID> {
    Iterable<T> findAll(Sort var1);

    Page<T> findAll(Pageable var1);
}
```

That means for our repositories, extend to **JpaRepository** will make them contain the full API of both **PagingAndSortingRepository** and **CrudRepository**.

Also, to use the full power of the __JpaRepository__, use the source code of jpa repository as a reference.
```java
// this means we can define a model-specified executor to execute queries
public interface JpaRepositoryImplementation<T, ID> extends JpaRepository<T, ID>, JpaSpecificationExecutor<T> {
    void setRepositoryMethodMetadata(CrudMethodMetadata var1);

    default void setEscapeCharacter(EscapeCharacter escapeCharacter) {
    }
}
```
Note that for an implementation of JpaRepository, we can extend it to __JpaRepository<ModelType, IDType>__, also, we can define a __JpaSpecificationExecutor<ModelType>__ to support our further queries.

It is very common for a model/data class to have date or datetime attributes that represents the date or time when the record is created or updated. Such attributes are commonly named as eg: createdAt, and modifiedAt/lastModifed. Spring Data provides corresponding support for these audition and attribute generation purposes. 

__@CreatedBy__ and __@LastModifiedBy__ annotation to capture who created or modified the entity.
__@CreatedDate__ and __@LastModifiedDate__ annotation to capture when the change happened. 

We can apply these annotations selectively depending on which information we want to capture.

We can also use domain class to implement the Auditable interface. 

