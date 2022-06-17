--Fetch number of first message sent in a conversation in a day. Date range - 1st Jan 2021 to 31st Dec 2021
SELECT
    date_,
    SUM(count_)
FROM
    (
        SELECT
            to_date(to_char(c.created_at, 'DD-MM-YYYY'))            AS date_,
            COUNT(DISTINCT m.conversation_id)                      AS count_
        FROM
            conversations  c, messages      m
        WHERE
                c.id = m.conversation_id
            AND to_date(to_char(c.created_at, 'DD-MM-YYYY')) BETWEEN '01-01-21' AND '31-12-21'
        GROUP BY
            to_date(to_char(c.created_at, 'DD-MM-YYYY')), m.conversation_id
        HAVING
            COUNT(m.id) >= 1
        order by 1
    )
GROUP BY
    date_;
    
    
--Fetch number of first reply message sent in a conversation in a day. Date range - 1st Jan 2021 to 31st Dec 2021
SELECT
    date_,
    SUM(count_)
FROM
    (
        SELECT
            to_date(to_char(c.created_at, 'DD-MM-YYYY'))            AS date_,
            COUNT(DISTINCT m.conversation_id)                      AS count_
        FROM
            conversations  c, messages      m
        WHERE
                c.id = m.conversation_id
            AND to_date(to_char(c.created_at, 'DD-MM-YYYY')) BETWEEN '01-01-21' AND '31-12-21'
        GROUP BY
            to_date(to_char(c.created_at, 'DD-MM-YYYY')), m.conversation_id
        HAVING
            COUNT(m.id) >= 2
        order by 1
    )
GROUP BY
    date_;
    
    
    
--Total conversation with 3 way messaging. 3 way messaging means User1 sent the message, then User2 replied and finally User1 messaged back.
SELECT
    date_,
    SUM(count_)
FROM
    (
        SELECT
            to_date(to_char(c.created_at, 'DD-MM-YYYY'))            AS date_,
            COUNT(DISTINCT m.conversation_id)                      AS count_
        FROM
            conversations  c, messages      m
        WHERE
                c.id = m.conversation_id
            AND to_date(to_char(c.created_at, 'DD-MM-YYYY')) BETWEEN '01-01-21' AND '31-12-21'
        GROUP BY
            to_date(to_char(c.created_at, 'DD-MM-YYYY')), m.conversation_id
        HAVING
            COUNT(m.id) >= 3
        order by 1
    )
GROUP BY
    date_;
