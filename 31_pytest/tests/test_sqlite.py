import pytest
import sqlite3


@pytest.fixture(scope="module")
def db_connection(request):
    """Create a SQLite database connection for testing."""
    print("db_connection", request)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE users
                 (username TEXT, email TEXT)"""
    )
    conn.commit()

    def teardown():
        print("teardown")
        """Close the database connection after the test."""
        conn.close()

    request.addfinalizer(teardown)
    return conn


@pytest.fixture(scope="function")
def per_function(request):
    print("per_function", request)


def create_user(conn, username, email):
    """Create a new user in the database."""
    print("create_user")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, email))
    conn.commit()


def update_email(conn, username, new_email):
    """Update user's email in the database."""
    print("update_email")
    c = conn.cursor()
    c.execute("UPDATE users SET email = ? WHERE username = ?", (new_email, username))
    conn.commit()


def test_create_user(db_connection):
    """Validate the creation of a new user in the database."""
    create_user(db_connection, "user1", "user1@example.com")
    # Verify the user's presence in the database
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", ("user1",))
    result = cursor.fetchone()
    assert result is not None  # Confirm the user's existence
    assert result[1] == "user1@example.com"  # Confirm the correct email of the user


def test_update_email(db_connection):
    """Check the update of a user's email in the database."""
    create_user(db_connection, "user2", "user2@example.com")
    update_email(db_connection, "user2", "new_email@example.com")
    # Confirm the email update in the database
    cursor = db_connection.cursor()
    cursor.execute("SELECT email FROM users WHERE username=?", ("user2",))
    result = cursor.fetchone()
    assert result is not None  # Confirm the user's existence
    assert result[0] == "new_email@example.com"  # Confirm the updated email
