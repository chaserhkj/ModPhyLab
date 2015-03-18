void analyze()
{
    TGraphErrors * tge = new TGraphErrors("data.txt", "%lg %lg %lg");
    tge->SetMarkerStyle(kOpenCircle);
    tge->SetMarkerColor(kBlack);
    tge->SetLineColor(kBlack);
    tge->SetTitle("; Atomic Number of Sample [Z] ; Peak Position / N");
    TF1 * f = new TF1("pdf", "[0]*(x-[1])^2 + [2]", 0, 100);
    TFitResultPtr res = tge->Fit(f, "S");
    res->Print();
    tge->DrawClone("APE");
    f->DrawClone("Same");

    TLegend * tl = new TLegend(.1, .7, .4, .9);
    tl->SetFillColor(0);
    tge->SetFillColor(0);
    tl->SetTextSize(.05);
    tl->AddEntry(tge, "Exp. Points");
    tl->AddEntry(f, "Fitted Line");
    tl->DrawClone("Same");
}
