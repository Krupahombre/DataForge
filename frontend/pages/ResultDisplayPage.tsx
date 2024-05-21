import React, { useState, useEffect, use } from "react";
import getData from "../common/services/getGeneratedData";
import IDisplayDataRecord from "../common/models/IDisplayDataRecord";
import styles from "../styles/Home.module.css";
import { useRouter } from "next/router";
import type { NextPage } from "next";
import NavBar from "../components/NavBar";

const ResultDisplayPage: NextPage = () => {
  const [data, setData] = useState<IDisplayDataRecord[]>(
    [] as IDisplayDataRecord[]
  );
  const [tabSelected, setTabSelected] = useState<string>("");
  const [copied, setCopied] = useState(false);

  const router = useRouter();

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const stringRequestTables = localStorage.getItem("requestTables");
    const stringFormatFilters = localStorage.getItem("formatFilters");
    if (stringRequestTables && stringFormatFilters) {
      const requestTables = JSON.parse(stringRequestTables);
      const formatFilters = JSON.parse(stringFormatFilters);

      const response = await getData(requestTables, formatFilters);
      if (stringFormatFilters == `"JSON"` || stringFormatFilters == `"PSQL"`) {
        const data = formatedJsonData(response);
        setData(data);
        setTabSelected(data?.[0]?.name || "");
      } else {
        const data = formatedData(response);
        setData(data);
        setTabSelected(data?.[0]?.name || "");
      }
    }
  };

  const handleBack = () => {
    router.push("/");
  };

  const formatedJsonData = (response: IDisplayDataRecord[]) => {
    if (response) {
      const formatedStringData = response.map((record) => {
        const formattedResponse = JSON.stringify(
          JSON.parse(record.response),
          null,
          2
        );

        return {
          name: record.name,
          response: formattedResponse,
        };
      });
      return formatedStringData;
    }
  };

  const formatedData = (response: IDisplayDataRecord[]) => {
    if (response) {
      const formatedStringData = response.map((record) => {
        const formattedResponse = record.response
          .replace(/;/g, ";\n")
          .replace(/CREATE/g, "\nCREATE")
          .replace(/INSERT/g, "\nINSERT")
          .replace(/DROP/g, "\nDROP")
          .replace(/VALUES/g, "\nVALUES");

        return {
          name: record.name,
          response: formattedResponse,
        };
      });
      return formatedStringData;
    }
  };

  const toggleTabSelected = (name: string) => {
    setTabSelected(name);
  };

  const copyToClipboard = (record) => {
    navigator.clipboard.writeText(record);
    setCopied(true);
    setTimeout(() => {
      setCopied(false);
    }, 1500);
  };
  const [highlightedLine, setHighlightedLine] = useState<number | null>(null);

  return (
    <div className={styles.mainDiv}>
      <NavBar />
      <div className={styles.gridContainer}>
        <div>
          <button className={styles.returnBtn} onClick={handleBack}>
            <span>Return</span>
            <svg
              viewBox="-5 -5 110 110"
              preserveAspectRatio="none"
              aria-hidden="true"
            >
              <path d="M0,0 C0,0 100,0 100,0 C100,0 100,100 100,100 C100,100 0,100 0,100 C0,100 0,0 0,0" />
            </svg>
          </button>
        </div>
        <div>
          <h1 className={styles.resultDisplayTitle}>Generated Data</h1>
        </div>
        <div></div>
      </div>
      {data && (
        <div className={styles.tabsContainer}>
          <div className={styles.resultAllTab}>
            {data.map((record) => (
              <div
                key={record.name}
                className={
                  tabSelected == record.name.toString()
                    ? styles.activeTabs
                    : styles.tabs
                }
                onClick={() => toggleTabSelected(record.name)}
              >
                {record.name}
              </div>
            ))}
          </div>
          <div className={styles.contentTabs}>
            {data.map((record) => (
              <div
                key={record.name}
                className={
                  tabSelected == record.name.toString()
                    ? styles.activeContent
                    : styles.content
                }
              >
                <div className={styles.btnDiv}>
                  <button
                    className={styles.copyBtn}
                    onClick={() => copyToClipboard(record.response)}
                  >
                    {copied ? "Copied" : "Copy to Clipboard"}
                  </button>
                </div>
                <div className={styles.responseDiv}>
                  <div className={styles.lineNumberingDiv}>
                    {record.response.split("\n").map((line, index) => (
                      <div
                        key={index}
                        className={`${styles.lineNumber} ${
                          highlightedLine === index ? styles.highlighted : ""
                        }`}
                        onMouseEnter={() => setHighlightedLine(index)}
                        onMouseLeave={() => setHighlightedLine(null)}
                      >
                        {index + 1}
                      </div>
                    ))}
                  </div>
                  <pre className={styles.resultContentCode}>
                    {record.response.split("\n").map((line, index) => (
                      <div
                        key={index}
                        className={
                          highlightedLine === index ? styles.highlighted : ""
                        }
                        onMouseEnter={() => setHighlightedLine(index)}
                        onMouseLeave={() => setHighlightedLine(null)}
                      >
                        {line}
                      </div>
                    ))}
                  </pre>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default ResultDisplayPage;
