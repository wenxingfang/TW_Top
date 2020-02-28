{
//=========Macro generated from canvas: c1/c1
//=========  (Fri May  9 21:17:09 2014) by ROOT version5.34/10
   TCanvas *c1 = new TCanvas("c1", "c1",65,24,1126,743);
   c1->Range(0,0,1,1);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   TArrow *arrow = new TArrow(0.05,0.9,0.35,0.5,0.02,"-|>-");
   arrow->SetFillColor(1);
   arrow->SetLineWidth(6);
   arrow->SetFillStyle(1001);
   arrow->Draw();
   TArrow *arrow = new TArrow(0.35,0.5,0.65,0.5,0.02,"-|>-");
   arrow->SetFillColor(1);
   arrow->SetLineWidth(6);
   arrow->SetFillStyle(1001);
   arrow->Draw();
  TCurlyLine *curlyline = new TCurlyLine(0.35,0.5,0.05,0.1,0.04,0.02);
   curlyline->SetLineWidth(6);
   curlyline->Draw();
  TArrow *arrow = new TArrow(0.65,0.5,0.95,0.9,0.02,"-|>-");
  arrow->SetFillColor(4);
   arrow->SetLineColor(4);
   arrow->SetLineWidth(6);
   arrow->SetFillStyle(1001);
   arrow->Draw();
  TCurlyLine *curlyline = new TCurlyLine(0.95,0.1,0.65,0.5,0.04,0.02);
   curlyline->SetLineWidth(6);
   curlyline->SetWavy();
   curlyline->Draw();
  TMarker *marker = new TMarker(0.65,0.5,20);
   marker->SetMarkerColor(2);
   marker->SetMarkerStyle(20);
   marker->SetMarkerSize(5);
   marker->Draw();
     TLatex *   tex = new TLatex(0.15,0.8,"u/c");
   tex->SetTextSize(0.12);
   tex->SetLineWidth(2);
   tex->SetTextFont(22);
   tex->Draw();

     TLatex *   tex = new TLatex(0.45,0.55,"u/c");
   tex->SetTextSize(0.12);
   tex->SetLineWidth(2);
   tex->SetTextFont(22);
   tex->Draw();

      tex = new TLatex(0.15,0.1,"g");
   tex->SetTextSize(0.12);
   tex->SetLineWidth(2);
   tex->SetTextFont(22);
   tex->Draw();
      tex = new TLatex(0.8,0.8,"t");
   tex->SetTextColor(4);
   tex->SetTextSize(0.12);
   tex->SetLineWidth(2);
   tex->SetTextFont(22);
   tex->Draw();
      tex = new TLatex(0.8,0.1,"#gamma");
   tex->SetTextSize(0.12);
   tex->SetLineWidth(2);
   tex->SetTextFont(22);
   tex->Draw();
  
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
   c1->ToggleToolBar();
}
