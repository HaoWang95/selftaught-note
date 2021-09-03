# **JUnit**

*JUnit5 = JUnit Platform + JUnit Jupiter + JUnit Vintage*

The **JUnit Platform** serves as the foundation for launching testing framework on the **JVM**. It also defines the TestEngine API. The platform provides a **Console Launcher** to launch the platform from the command line and a **Junit 4 based runner** for running any TestEngine on the platform in a Junit 4 based env.

**JUnit Jupiter** is the combination of the **programming model** and **extension model** for writing tests and extensions in Junit 5.

**JUnit Vintage** provides TestEngine for running JUnit 3 and JUnit 4 based tests.

## JUnit Annotations
All core annotations can be imported from org.junit.jupiter.api package.
> - @Test Denote a method is a test method
> - @ParameterizedTest
> - @RepeatedTest
> - @TestFactory Denote a method is a test factory for **dynamic tests**. Inherited unless they are overriden.
> - @TestTemplate Denote a method is a template for test cases.
> - @TestMethodOrder
> - @TestInstance
> - @DisplayName
> - @DisplayNameGeneration
> - @BeforeEach
> - @AfterEach
> - @BeforeAll Must be **static**
> - @AfterAll Must be **static**
> - @Nested The annotated class is a non-static nested test class.
> - @Tag Declare **tags for filtering tests**, either at the class or method level.
> - @Disabled **Disable** a test class or a test method. Analogous to JUnit4's @Ignore.
> - @Timeout 
> - @ExtendWith
> - @RegisterExtension
> - @TempDir


Besides JUnit annotations above, **java.lang.annotation** can be used for annotation composition.

### @Nested
@Nested tests give the test writer more capabilities to express the relationship among several groups of tests. 