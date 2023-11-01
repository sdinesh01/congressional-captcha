SQL_BILLS_BUILD = """
            CREATE TABLE tBills
            (
                bill_id INTEGER NOT NULL PRIMARY KEY,
                bill_number INTEGER NOT NULL,
                title TEXT,
                description TEXT,
                state TEXT NOT NULL, 
                session TEXT NOT NULL, 
                filename TEXT NOT NULL, 
                status INTEGER NOT NULL,
                status_date TEXT, 
                url TEXT, 
                error TEXT,
                content TEXT
            );"""

SQL_CHECK_BILLS = """
            SELECT bill_id
            FROM tBills
            WHERE bill_number = :bill_number
                AND title = :title
                AND description = :description
                AND state = :state
                AND session = :session
                AND filename = :filename
                AND status = :status
                AND status_date = :status_date
                AND url = :url
            ;"""

SQL_INSERT_TBILLS = """
            INSERT INTO tBills (
                            bill_id,
                            bill_number,
                            title,
                            description, 
                            state,
                            session,
                            filename, 
                            status, 
                            status_date,
                            url, 
                            error,
                            content)
            VALUES (:bill_id,
                    :bill_number,
                    :title,
                    :description,
                    :state, 
                    :session, 
                    :filename, 
                    :status, 
                    :status_date, 
                    :url,
                    :error,
                    :content
                    )
            ;"""
