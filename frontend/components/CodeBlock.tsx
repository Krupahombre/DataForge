import React, { useState } from "react";
import AceEditor from "react-ace";
import styles from "../styles/Home.module.css";

import "ace-builds/src-noconflict/mode-sql";
import "ace-builds/src-noconflict/theme-solarized_light";

const CodeBlock: React.FC<{ record; format }> = ({ record, format }) => {
  const [highlightedLine, setHighlightedLine] = useState<number | null>(null);

  return (
    <AceEditor
      mode={format}
      theme="solarized_light"
      fontSize={14}
      width="100%"
      height="500px"
      showGutter={true}
      highlightActiveLine={true}
      editorProps={{ $blockScrolling: Infinity }}
      value={record}
      readOnly={true}
      wrapEnabled={true}
      onSelectionChange={(_, selection) => {
        if (selection && selection.start) {
          setHighlightedLine(selection.start.row);
        }
      }}
    />
  );
};

export default CodeBlock;
