#!/usr/bin/env node
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";

const root = path.resolve(path.join(import.meta.dirname, "..", ".."));
const sourceDraft = path.join(root, "design", "tests", "visual-learning-lab-social-scheduler-test-2026-06-28.md");
const env = process["env"];
const defaultExportRoot = path.join(env.HOME || ".", "Desktop");
const outDir =
  env.OCI_DESIGN_EXPORT_DIR ||
  path.join(defaultExportRoot, "oci-design-visual-learning-share-images-2026-06-28");
const slintViewer =
  env.OCI_SLINT_VIEWER ||
  `${env.TMPDIR || "/tmp"}/oci-slint-v1.17.0/bin/slint-viewer/slint-viewer`;

const cards = [
  {
    day: "01",
    slug: "ai-referral-traffic-map",
    title: "AI Traffic Is Small. The Signal Is Not.",
    eyebrow: "Visual Learning Lab / research remix",
    theme: "AI visibility becomes useful when it is measured.",
    proof: ["Track source", "Landing page", "Engaged time", "Conversion"],
    takeaway: "Teams that learn the signal early move with better evidence.",
    visual: "traffic",
  },
  {
    day: "02",
    slug: "flow-arrows-for-ai-adoption",
    title: "AI Adoption Is Movement.",
    eyebrow: "OCI Design / workflow map",
    theme: "Draw the workflow before buying another tool.",
    proof: ["Start", "Handoff", "Approval", "Value"],
    takeaway: "Automate the arrow that earns the right to get thicker.",
    visual: "flow",
  },
  {
    day: "03",
    slug: "deliberate-practice-ai-learning-loop",
    title: "Watching AI Tips Is Not Learning AI.",
    eyebrow: "Visual Learning Lab / skill loop",
    theme: "One repeated workflow beats ten random tricks.",
    proof: ["Baseline", "Practice", "Score", "Adjust"],
    takeaway: "Skill is the workflow that survives repetition.",
    visual: "loop",
  },
  {
    day: "04",
    slug: "venn-diagram-ai-debugging",
    title: "Bad AI Output Rarely Has One Cause.",
    eyebrow: "OCI Design / debugging map",
    theme: "Look for overlap before blaming the model.",
    proof: ["Prompt", "Context", "Data", "Eval"],
    takeaway: "Fix the smallest cause you can prove.",
    visual: "venn",
  },
  {
    day: "05",
    slug: "llm-benchmark-literacy",
    title: "A Leaderboard Is Not A Business Case.",
    eyebrow: "Visual Learning Lab / model scorecard",
    theme: "Benchmarks create the shortlist. Workflow evals make the decision.",
    proof: ["Quality", "Latency", "Cost", "Risk"],
    takeaway: "Choose the model that passes your task under your constraints.",
    visual: "scorecard",
  },
];

function q(value) {
  return JSON.stringify(value);
}

function rect({ x, y, w, h, bg = "#ffffff", border = "", radius = 0, opacity = 1 }) {
  return `Rectangle { x: ${x}px; y: ${y}px; width: ${w}px; height: ${h}px; background: ${bg}; border-radius: ${radius}px; ${border ? `border-color: ${border}; border-width: 1px;` : ""} opacity: ${opacity}; }`;
}

function text({ x, y, w, body, size = 32, color = "#312d2a", weight = 400, wrap = true }) {
  return `Text { x: ${x}px; y: ${y}px; width: ${w}px; text: ${q(body)}; color: ${color}; font-size: ${size}px; font-weight: ${weight}; ${wrap ? "wrap: word-wrap;" : ""} }`;
}

function label(x, y, body) {
  return `${rect({ x, y, w: 182, h: 48, bg: "#fbf9f7", border: "#e2d8d0", radius: 24 })}
${text({ x: x + 22, y: y + 13, w: 140, body, size: 18, color: "#5f5750", weight: 600, wrap: false })}`;
}

function trafficVisual() {
  return `
${rect({ x: 88, y: 670, w: 904, h: 300, bg: "#ffffff", border: "#e2d8d0", radius: 14 })}
${text({ x: 118, y: 704, w: 600, body: "Measure the signal", size: 28, weight: 700 })}
${label(118, 770, "source")}
${label(334, 770, "page")}
${label(550, 770, "time")}
${label(766, 770, "conversion")}
${rect({ x: 124, y: 880, w: 116, h: 26, bg: "#d8d2ca", radius: 13 })}
${rect({ x: 264, y: 856, w: 166, h: 50, bg: "#c74634", radius: 25 })}
${rect({ x: 454, y: 826, w: 222, h: 80, bg: "#312d2a", radius: 40 })}
${rect({ x: 724, y: 848, w: 214, h: 70, bg: "#7f4f3f", radius: 35 })}
${text({ x: 760, y: 870, w: 160, body: "16x growth signal", size: 22, color: "#ffffff", weight: 700 })}
`;
}

function flowVisual() {
  return `
${rect({ x: 88, y: 674, w: 904, h: 292, bg: "#ffffff", border: "#e2d8d0", radius: 14 })}
${text({ x: 118, y: 710, w: 640, body: "Map the movement", size: 28, weight: 700 })}
${rect({ x: 124, y: 798, w: 180, h: 92, bg: "#fbf9f7", border: "#d8d2ca", radius: 12 })}
${text({ x: 154, y: 827, w: 120, body: "Current work", size: 22, weight: 700 })}
${text({ x: 340, y: 832, w: 120, body: "->", size: 48, color: "#c74634", weight: 700, wrap: false })}
${rect({ x: 452, y: 798, w: 180, h: 92, bg: "#fbf9f7", border: "#d8d2ca", radius: 12 })}
${text({ x: 484, y: 827, w: 128, body: "Human gate", size: 22, weight: 700 })}
${text({ x: 668, y: 832, w: 120, body: "->", size: 48, color: "#c74634", weight: 700, wrap: false })}
${rect({ x: 780, y: 780, w: 170, h: 128, bg: "#c74634", radius: 18 })}
${text({ x: 813, y: 818, w: 120, body: "AI assisted path", size: 22, color: "#ffffff", weight: 700 })}
`;
}

function loopVisual() {
  return `
${rect({ x: 88, y: 674, w: 904, h: 300, bg: "#ffffff", border: "#e2d8d0", radius: 14 })}
${text({ x: 118, y: 710, w: 640, body: "Practice loop", size: 28, weight: 700 })}
${label(126, 808, "baseline")}
${label(324, 760, "practice")}
${label(522, 808, "score")}
${label(720, 760, "adjust")}
${text({ x: 268, y: 818, w: 80, body: "->", size: 36, color: "#c74634", weight: 700, wrap: false })}
${text({ x: 466, y: 818, w: 80, body: "->", size: 36, color: "#c74634", weight: 700, wrap: false })}
${text({ x: 664, y: 818, w: 80, body: "->", size: 36, color: "#c74634", weight: 700, wrap: false })}
${text({ x: 430, y: 908, w: 260, body: "repeat x10", size: 28, color: "#c74634", weight: 800 })}
`;
}

function vennVisual() {
  return `
${rect({ x: 88, y: 674, w: 904, h: 310, bg: "#ffffff", border: "#e2d8d0", radius: 14 })}
${text({ x: 118, y: 710, w: 660, body: "Debug the overlap", size: 28, weight: 700 })}
Rectangle { x: 228px; y: 770px; width: 190px; height: 190px; background: #f0d7cf; border-radius: 95px; opacity: 0.82; }
Rectangle { x: 368px; y: 770px; width: 190px; height: 190px; background: #ded8cf; border-radius: 95px; opacity: 0.82; }
Rectangle { x: 508px; y: 770px; width: 190px; height: 190px; background: #c8d6d0; border-radius: 95px; opacity: 0.82; }
Rectangle { x: 648px; y: 770px; width: 190px; height: 190px; background: #e7dcc7; border-radius: 95px; opacity: 0.82; }
${text({ x: 260, y: 848, w: 130, body: "prompt", size: 20, weight: 700 })}
${text({ x: 398, y: 848, w: 130, body: "context", size: 20, weight: 700 })}
${text({ x: 554, y: 848, w: 90, body: "data", size: 20, weight: 700 })}
${text({ x: 696, y: 848, w: 100, body: "eval", size: 20, weight: 700 })}
`;
}

function scorecardVisual() {
  return `
${rect({ x: 88, y: 674, w: 904, h: 310, bg: "#ffffff", border: "#e2d8d0", radius: 14 })}
${text({ x: 118, y: 710, w: 640, body: "Score the fit", size: 28, weight: 700 })}
${rect({ x: 122, y: 782, w: 390, h: 82, bg: "#fbf9f7", border: "#d8d2ca", radius: 12 })}
${text({ x: 152, y: 807, w: 300, body: "Benchmark -> shortlist", size: 24, weight: 700 })}
${rect({ x: 568, y: 782, w: 390, h: 82, bg: "#c74634", radius: 12 })}
${text({ x: 598, y: 807, w: 300, body: "Workflow eval -> decision", size: 24, color: "#ffffff", weight: 700 })}
${label(132, 908, "quality")}
${label(332, 908, "latency")}
${label(532, 908, "cost")}
${label(732, 908, "risk")}
`;
}

function visual(card) {
  if (card.visual === "traffic") return trafficVisual();
  if (card.visual === "flow") return flowVisual();
  if (card.visual === "loop") return loopVisual();
  if (card.visual === "venn") return vennVisual();
  return scorecardVisual();
}

function cardSource(card) {
  return `export component ShareCard inherits Window {
    title: ${q(`OCI Design - ${card.title}`)};
    width: 1080px;
    height: 1350px;
    background: #f8f6f3;

    ${rect({ x: 0, y: 0, w: 1080, h: 1350, bg: "#f8f6f3" })}
    ${rect({ x: 0, y: 0, w: 1080, h: 28, bg: "#c74634" })}
    ${rect({ x: 56, y: 70, w: 968, h: 1210, bg: "#ffffff", border: "#d8d2ca", radius: 18 })}
    ${rect({ x: 88, y: 118, w: 178, h: 46, bg: "#312d2a", radius: 23 })}
    ${text({ x: 116, y: 131, w: 130, body: `DAY ${card.day}`, size: 18, color: "#ffffff", weight: 800, wrap: false })}
    ${text({ x: 296, y: 128, w: 660, body: card.eyebrow, size: 20, color: "#6f6861", weight: 600 })}
    ${text({ x: 88, y: 220, w: 880, body: card.title, size: 58, color: "#312d2a", weight: 800 })}
    ${text({ x: 88, y: 426, w: 840, body: card.theme, size: 32, color: "#5f5750", weight: 600 })}
    ${visual(card)}
    ${text({ x: 92, y: 1040, w: 820, body: card.takeaway, size: 38, color: "#312d2a", weight: 800 })}
    ${rect({ x: 88, y: 1188, w: 904, h: 1, bg: "#e5ded7" })}
    ${text({ x: 88, y: 1220, w: 560, body: "OCI Design / Visual Learning Lab", size: 22, color: "#6f6861", weight: 700 })}
    ${text({ x: 700, y: 1220, w: 290, body: "public-safe research remix", size: 20, color: "#8a8178", weight: 600 })}
}`;
}

function ensureCleanDir(dir) {
  fs.rmSync(dir, { recursive: true, force: true });
  fs.mkdirSync(dir, { recursive: true });
}

function main() {
  if (!fs.existsSync(sourceDraft)) {
    throw new Error(`Missing social instructions: ${sourceDraft}`);
  }
  if (!fs.existsSync(slintViewer)) {
    throw new Error(`Missing slint-viewer: ${slintViewer}`);
  }

  ensureCleanDir(outDir);
  const slintDir = path.join(outDir, "slint-sources");
  fs.mkdirSync(slintDir, { recursive: true });

  fs.copyFileSync(sourceDraft, path.join(outDir, path.basename(sourceDraft)));

  const manifest = [];
  for (const card of cards) {
    const base = `${card.day}-${card.slug}`;
    const slintPath = path.join(slintDir, `${base}.slint`);
    const pngPath = path.join(outDir, `${base}.png`);
    fs.writeFileSync(slintPath, cardSource(card));
    execFileSync(slintViewer, ["--style", "fluent", "--screenshot", pngPath, slintPath], {
      stdio: "inherit",
    });
    manifest.push({ ...card, png: pngPath, slint: slintPath });
  }

  fs.writeFileSync(
    path.join(outDir, "README.md"),
    `# OCI Design Visual Learning Share Images - 2026-06-28

These are finalized PNG share cards generated from the Visual Learning Lab research pack and the OCI Design Slint lane.

## Images

${manifest.map((item) => `- \`${path.basename(item.png)}\` - ${item.title}`).join("\n")}

## Source

- Social post Markdown instructions: \`${path.basename(sourceDraft)}\`
- Slint sources: \`slint-sources/\`

The PNGs are 1080x1350 portrait cards suitable for Instagram, LinkedIn, and X.com preview sharing.
`
  );

  fs.writeFileSync(path.join(outDir, "manifest.json"), `${JSON.stringify(manifest, null, 2)}\n`);
  console.log(outDir);
  console.log(`Rendered ${manifest.length} PNG files.`);
}

main();
