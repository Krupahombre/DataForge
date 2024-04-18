import React, { useState, useEffect, use } from "react";
import getData from "../../common/services/getGeneratedData";
import IResponse from "../../common/models/IResponse";
import styles from "../../styles/Home.module.css";

const ResultDisplayPage = () => {
  const [data, setData] = useState<IResponse>(null);
  const [formattedIban, setFormattedIban] = useState(null);
  const [formattedPerson, setFormattedPerson] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const response = await getData();
    console.log(response);
    setData(response);
  };

  useEffect(() => {
    formatData();
  }, [data]);

  const formatData = () => {
    if (data) {
      const formattedSql = data.iban
        .toString()
        .replace(/;/g, ";\n") // Dodaj nową linię po każdym średniku
        .replace(/CREATE/g, "\nCREATE") // Dodaj nową linię przed CREATE
        .replace(/INSERT/g, "\nINSERT") // Dodaj nową linię przed INSERT
        .replace(/DROP/g, "\nDROP") // Dodaj nową linię przed DROP
        .replace(/VALUES/g, "\nVALUES"); // Dodaj nową linię przed VALUES

      setFormattedIban(formattedSql);
      const formattedSqlPerson = data.person
        .toString()
        .replace(/;/g, ";\n") // Dodaj nową linię po każdym średniku
        .replace(/CREATE/g, "\nCREATE") // Dodaj nową linię przed CREATE
        .replace(/INSERT/g, "\nINSERT") // Dodaj nową linię przed INSERT
        .replace(/DROP/g, "\nDROP") // Dodaj nową linię przed DROP
        .replace(/VALUES/g, "\nVALUES"); // Dodaj nową linię przed VALUES

      setFormattedPerson(formattedSqlPerson);
    }
  };

  return (
    <div className={styles.mainDiv}>
      <h1 className={styles.resultDisplayTitle}>Generated Data</h1>
      {data && (
        <div className={styles.resultCodeDisplay}>
          <div>
            <p className={styles.resultDisplay}>Person</p>
            <pre className={styles.resultPDisplay}>{formattedPerson}</pre>
          </div>
          <div>
            <p className={styles.resultDisplay}>IBAN</p>
            <pre className={styles.resultPDisplay}>{formattedIban}</pre>
          </div>
        </div>
      )}
    </div>
  );
};

export default ResultDisplayPage;
