This note will include __CrudRepository__, __JpaRepository__ and __PagingAndSortingRepository__.

The **JpaRepository** extends the **PagingAndSortingRepository**.

```java

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
public interface JpaRepositoryImplementation<T, ID> extends JpaRepository<T, ID>, JpaSpecificationExecutor<T> {
    void setRepositoryMethodMetadata(CrudMethodMetadata var1);

    default void setEscapeCharacter(EscapeCharacter escapeCharacter) {
    }
}
```
Note that for an implementation of JpaRepository, we can extend it to JpaRepository<ModelType, IDType>, also, we can define a JpaSpecificationExecutor<ModelType> to support our further queries.

