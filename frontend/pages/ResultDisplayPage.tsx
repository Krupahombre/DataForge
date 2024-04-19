import React, { useState, useEffect, use } from "react";
import getData from "../common/services/getGeneratedData";
import IResponse from "../common/models/IResponse";
import styles from "../styles/Home.module.css";
import { useRouter } from "next/router";

const ResultDisplayPage = () => {
  const [data, setData] = useState<IResponse>(null);
  const [formattedIban, setFormattedIban] = useState(null);
  const [formattedPerson, setFormattedPerson] = useState(null);

  const router = useRouter();

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
        .replace(/;/g, ";\n")
        .replace(/CREATE/g, "\nCREATE")
        .replace(/INSERT/g, "\nINSERT")
        .replace(/DROP/g, "\nDROP")
        .replace(/VALUES/g, "\nVALUES");

      setFormattedIban(formattedSql);
      const formattedSqlPerson = data.person
        .toString()
        .replace(/;/g, ";\n")
        .replace(/CREATE/g, "\nCREATE")
        .replace(/INSERT/g, "\nINSERT")
        .replace(/DROP/g, "\nDROP")
        .replace(/VALUES/g, "\nVALUES");

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
